# 📊 LeetCode SQL 50

[![LeetCode SQL 50](https://img.shields.io/badge/Study%20Plan-SQL%2050-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/study-plan/v2/top-sql-50)
[![Automation](https://img.shields.io/badge/README-Automated-007ACC?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Language](https://img.shields.io/badge/Language-ANSI%20SQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://en.wikipedia.org/wiki/SQL)

---

## 📈 The scoreboard

This table is auto-generated — don't edit it by hand, it'll just get overwritten anyway 🙂

<!-- leetcode_sql:START -->
<details open>
<summary>LeetCode SQL Practice (17)</summary>

| # | Problem | Link |
|---|---------|------|
| 1 | AverageTimeofProcessperMachine | [Code](solutions/166.AverageTimeofProcessperMachine.sql) |
| 2 | RisingTemperature | [Code](solutions/197.RisingTemperature.sql) |
| 3 | ManagerswithatLeast5DirectReports | [Code](solutions/570.ManagerswithatLeast5DirectReports.sql) |
| 4 | FindCustomerReferee | [Code](solutions/584.FindCustomerReferee.sql) |
| 5 | BigCountries | [Code](solutions/595.BigCountries.sql) |
| 6 | NotBoringMovies | [Code](solutions/620.NotBoringMovies.sql) |
| 7 | ProductSalesAnalysisI | [Code](solutions/1068.ProductSalesAnalysisI.sql) |
| 8 | ProjectEmployeesI | [Code](solutions/1075.ProjectEmployeesI.sql) |
| 9 | ArticleViewsI | [Code](solutions/1148.ArticleViewsI.sql) |
| 10 | QueriesQualityandPercentage | [Code](solutions/1211.QueriesQualityandPercentage.sql) |
| 11 | AverageSellingPrice | [Code](solutions/1251.AverageSellingPrice.sql) |
| 12 | ReplaceEmployeeIDWithTheUniqueIdentifier | [Code](solutions/1378.ReplaceEmployeeIDWithTheUniqueIdentifier.sql) |
| 13 | CustomerWhoVisitedbutDidNotMakeAnyTransactions | [Code](solutions/1581.CustomerWhoVisitedbutDidNotMakeAnyTransactions.sql) |
| 14 | PercentageofUsersAttendedaContest | [Code](solutions/1633.PercentageofUsersAttendedaContest.sql) |
| 15 | InvalidTweets | [Code](solutions/1683.InvalidTweets.sql) |
| 16 | RecyclableandLowFatProducts | [Code](solutions/1757.RecyclableandLowFatProducts.sql) |
| 17 | ConfirmationRate | [Code](solutions/1934.ConfirmationRate.sql) |
</details>
<!-- leetcode_sql:END -->

---

## 👋 What's this?

This is my little SQL gym. I'm working through LeetCode's **Top SQL 50** study plan, one query at a time, and dumping every solution here so I can watch the progress add up.

I'm not just trying to get a green checkmark — I actually enjoy the puzzle of it. How do you write a query that's not just *correct*, but clean, fast, and doesn't make the database cry? That's the fun part for me: joins, window functions, aggregations, all of it.

---

## ⚙️ How it stays up to date (without me lifting a finger)

I got a little lazy about manually updating a table every time I add a solution, so I automated it:

1. I drop a new `.sql` file into `/solutions/`.
2. I push it to GitHub.
3. A GitHub Action wakes up, runs `generate_table.py`, and it scans the folder, figures out the problem number and name from the filename, and rebuilds the table below.
4. It commits the updated README right back to the repo. No copy-pasting, no forgetting to update a count.

```
📂 repository-root
├── 📂 .github/workflows/    # the robot that runs the script on every push
├── 📂 solutions/            # all my actual .sql answers live here
├── 📄 generate_table.py     # reads the folder, writes the table below
└── 📄 README.md             # you are here
```

---

## 🛠️ Want to run this yourself?

If you're forking this to track your own SQL grind, here's the one rule that matters: **name your files like this** —

```
[ProblemNumber].[ProblemNameNoSpaces].sql
```

✅ `1757.RecyclableandLowFatProducts.sql`
❌ `1757_recyclable_products.sql` (wrong separator)
❌ `1757.sql` (needs a name too)

Then just run:

```bash
python generate_table.py
```

and check the README updated itself.

**Two things not to touch:** the `<!-- leetcode_sql:START -->` / `<!-- leetcode_sql:END -->` comments — those are how the script knows where to inject the table. And keep all your `.sql` files directly inside `/solutions/`, not in subfolders.

That's it — happy querying! 🐘