import java.util.*;

// ==================== Cell ====================

class Cell {
    private final String rawValue;      // what was set, e.g. "= A2 + B3 - 10"
    private String cachedValue;         // last computed result, e.g. "15"
    private final boolean isFormula;
    private final List<String> dependencies; // cell IDs this formula references

    public Cell(String rawValue) {
        this.rawValue = rawValue;
        this.isFormula = rawValue.trim().startsWith("=");
        this.dependencies = new ArrayList<>();

        if (isFormula) {
            parseDependencies(rawValue);
            this.cachedValue = ""; // computed later
        } else {
            this.cachedValue = rawValue;
        }
    }

    private void parseDependencies(String formula) {
        // "= A2 + B3 - 10" → tokens: ["A2", "+", "B3", "-", "10"]
        String expr = formula.substring(formula.indexOf('=') + 1).trim();
        for (String token : expr.split(" ")) {
            if (!token.isEmpty() && Character.isLetter(token.charAt(0))) {
                dependencies.add(token);
            }
        }
    }

    public boolean isFormula()               { return isFormula; }
    public String getRawValue()              { return rawValue; }
    public String getCachedValue()           { return cachedValue; }
    public void setCachedValue(String val)   { this.cachedValue = val; }
    public List<String> getDependencies()    { return dependencies; }
}

// ==================== Spreadsheet ====================

public class Spreadsheet {

    // cellId → Cell
    private final Map<String, Cell> cells = new HashMap<>();

    // reverse dependency graph: cellId → set of cells that depend ON it
    // e.g. if D3 = A2 + B1, then reverseDeps["A2"] contains "D3"
    private final Map<String, Set<String>> reverseDeps = new HashMap<>();

    // ---- Public API ----

    public void set(String cellId, String value) {
        // 1. Tear down old reverse-dep registrations for this cell
        Cell existing = cells.get(cellId);
        if (existing != null && existing.isFormula()) {
            for (String dep : existing.getDependencies()) {
                reverseDeps.getOrDefault(dep, Collections.emptySet()).remove(cellId);
            }
        }

        // 2. Store new cell
        Cell cell = new Cell(value);
        cells.put(cellId, cell);

        // 3. Register new reverse-dep edges
        if (cell.isFormula()) {
            for (String dep : cell.getDependencies()) {
                reverseDeps.computeIfAbsent(dep, k -> new HashSet<>()).add(cellId);
            }
        }

        // 4. Recompute this cell + all transitive dependents (BFS)
        recomputeFrom(cellId);
    }

    public String get(String cellId) {
        Cell cell = cells.get(cellId);
        return cell == null ? "" : cell.getCachedValue();
        // O(1) read — cache does the heavy lifting
    }

    // ---- Private helpers ----

    /**
     * BFS from the changed cell outward through the dependency graph.
     * Recomputes each formula cell it encounters.
     */
    private void recomputeFrom(String startId) {
        Queue<String> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();

        queue.add(startId);
        visited.add(startId);

        while (!queue.isEmpty()) {
            String current = queue.poll();
            Cell cell = cells.get(current);

            // Recompute this cell if it's a formula (skip the start cell if it's a raw value)
            if (cell != null && cell.isFormula()) {
                cell.setCachedValue(evaluateFormula(cell.getRawValue()));
            }

            // Enqueue all cells that depend on current
            for (String dependent : reverseDeps.getOrDefault(current, Collections.emptySet())) {
                if (!visited.contains(dependent)) {
                    visited.add(dependent);
                    queue.add(dependent);
                }
            }
        }
    }

    /**
     * Evaluates "= A2 + B3 - 10" left to right.
     * Resolves cell references recursively via get().
     */
    private String evaluateFormula(String formula) {
        String expr = formula.substring(formula.indexOf('=') + 1).trim();
        String[] tokens = expr.split(" ");

        int result = resolveOperand(tokens[0]);

        for (int i = 1; i < tokens.length - 1; i += 2) {
            String op      = tokens[i];
            int    operand = resolveOperand(tokens[i + 1]);

            if      (op.equals("+")) result += operand;
            else if (op.equals("-")) result -= operand;
        }

        return String.valueOf(result);
    }

    private int resolveOperand(String token) {
        if (Character.isLetter(token.charAt(0))) {
            // Cell reference — get its current cached value
            String val = get(token);
            return val.isEmpty() ? 0 : Integer.parseInt(val);
        }
        return Integer.parseInt(token);
    }

    // ---- Demo ----

    public static void main(String[] args) {
        Spreadsheet sheet = new Spreadsheet();

        sheet.set("A1", "10");
        sheet.set("B1", "20");
        sheet.set("C1", "= A1 + B1");   // 30
        sheet.set("D1", "= C1 - 5");    // 25

        System.out.println(sheet.get("C1")); // 30
        System.out.println(sheet.get("D1")); // 25

        // Now change A1 — C1 and D1 should update automatically
        sheet.set("A1", "50");

        System.out.println(sheet.get("C1")); // 70
        System.out.println(sheet.get("D1")); // 65

        // String value
        sheet.set("Z99", "Sunday");
        System.out.println(sheet.get("Z99")); // Sunday
    }
}