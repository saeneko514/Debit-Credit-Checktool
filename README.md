
## Journal Balance Checker

This tool reads a journal CSV file and checks whether the **debit and credit amounts balance** for each entry number (voucher).

---

## Input Format Example (`journal_sample.csv`)

| Number | Account       | Debit   | Credit  |
|--------|----------------|---------|---------|
| 1001   | Cash           | 10000   |         |
| 1001   | Sales          |         | 10000   |
| 1002   | Purchases      | 5000    |         |
| 1002   | Cash           |         | 6000    |

---

## How to Run

```bash
python validate_journal.py
Replace validate_journal.py with your actual filename.

✅ Output Example
If all entries are balanced:


✅ All journal entries are balanced.
If unbalanced entries exist:


⚠️ Unbalanced entries found:
   Number   Debit   Credit  Diff
   1002     5000     6000   -1000

"" Built With
Python 3
pandas
