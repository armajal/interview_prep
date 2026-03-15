public static main(String[] args) {
    System.out.println("hello world"); 
}
/*
    Questions:
        1. 1 <= Accout number <= n  (Offset of 1 bc [0, n-1] array)
            account number = index - 1 
        2. Can a balance be negative? 

    Intuition
        1. Long[] balance , index == account number, balance[index]

 */
class Bank {

    long[] balanceList;
    int accountNums; 

    public Bank(long[] balance) {
        this.balanceList = balance;
        this.accountNums = balance.length; 
    }
    
    public boolean transfer(int account1, int account2, long money) {
        if(balanceList[account1 - 1] <= money || account1 > accountNums || account2 > accountNums || account1 < 1 || account2 < 1 ){
            return false; 
        }

        balanceList[account1 - 1] -= money; 
        balanceList[account2 - 1] += money; 
        return true; 
    }
    
    public boolean deposit(int account, long money) {
        if( account > accountNums || account < 1 ){
            return false; 
        }

        balanceList[account - 1] += money; 
        return true; 
        
    }
    
    public boolean withdraw(int account, long money) {
        if( account > accountNums || account < 1 ){
            return false; 
        }
        
        balanceList[account - 1] -= money; 
        return true; 
        
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * Bank obj = new Bank(balance);
 * boolean param_1 = obj.transfer(account1,account2,money);
 * boolean param_2 = obj.deposit(account,money);
 * boolean param_3 = obj.withdraw(account,money);
 */