'''

Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, 
and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts.
 Note that even if two accounts have the same name, 
they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their 
accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the 
elements are emails in sorted order. 
The accounts themselves can be returned in any order.

----------------
Input: List of accounts : accounts[i]: [name, email, email, email...]
Output; merged_accounts[]: merged_accounts[i]: [name, aemail, bemail,...] | merge accounts and put under 1 name with all correpsonding emails
Constraint: two accounts are the same by email NOT by name.  
Tool: Union Find

Approach:
    1. email_to_name = {}
        parent_email_to_childd email = {}
    
    2. for each account in accounts_list:
            for email in account:
                accouns_obj(name, email)
                
                if any email in account exists in rank:

                    root_account = find(email that exists)
                    union(account_node, root_account)
                
                else 
                    account_node(email, name) -> parent of itself
            
    3. res = [] 
    for each parent_account:
        res.append(parent_account.name, parent.list_of_emails)
        
'''
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_email = {}
        email_to_name = {}

        def union(email: str, parent_email: str):
            email_to_email[find(parent_email)] = find(email)

        def find( email: str):
            if email_to_email[email] != email:
                email_to_email[email] = find(email_to_email[email])
            return email_to_email[email]

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email_to_email:
                    email_to_email[email] = email
                email_to_name[email] = name
                union(email, account[1])

        account_groups = defaultdict(list)

        for email in email_to_email:
            account_groups[find(email)].append(email)
        

        return [[email_to_name[root]] + sorted(email_list) for root, email_list in account_groups.items()]
        
