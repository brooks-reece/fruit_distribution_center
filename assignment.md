# Python Basics with Tuples, Dictionaries, and Sets

Welcome to your next assignment! In this activity, you’ll work **in a team** to create a small project that manages fruit inventory. You will use:

* Basic Python (simple variables, print statements, basic operations)
* Tuples
* Dictionaries
* Sets
* Git & GitHub for collaboration

We’ll imagine you and your teammates run a fruit distribution center and need to track inventory, pricing, and stock status. By the end of this assignment, your team will each have contributed different parts of the code and merged everything on GitHub.

---

## Scenario

Your fruit distribution center ships fruit orders to local grocery stores. You and your team need to:

* Keep track of fruit details (like name and price).
* Group fruits into batches using tuples.
* Store and update fruit information with dictionaries.
* Check which fruits are in stock or out of stock using sets.
* Collaborate using Git & GitHub by dividing the tasks among your teammates.

---

## Instructions

### 1. Set Up the Shared Repository

1. One person on your team should create a new GitHub repository called **`fruit_distribution_center`**.
2. Invite the other teammates as collaborators so each person can clone, commit, and push.

### 2. Create a Shared Jupyter Notebook

1. In your cloned repository, create a Jupyter notebook named **`fruit_inventory.ipynb`**.
2. At the top of the notebook, write a brief description:  
   * The purpose of this notebook (managing fruit data).
   * The tasks you need to complete as a team.

### 3. Define the Fruit Tuples (Team Member A)

1. Create a tuple named **`fruit_batch`** that contains **five** different fruit names (e.g., `"apples"`, `"bananas"`, `"cherries"`, etc.).
2. Print out the **`fruit_batch`** tuple to verify the contents.
3. Commit and push your changes with a descriptive message (e.g., “Add initial fruit tuple”).

### 4. Store and Update Fruit Details with Dictionaries (Team Member B)

1. Pull the latest changes from the repository so you have the updated notebook with `fruit_batch`.
2. Create a dictionary named **`fruit_details`** that maps **each fruit** in `fruit_batch` to a dictionary of details, such as:

   ```python
   fruit_details = {
       "apples": {"price_per_lb": 2.5, "color": "red", "in_stock": True},
       "bananas": {"price_per_lb": 1.2, "color": "yellow", "in_stock": True},
       ...
   }
   ```

   * Feel free to include any details you like (price, color, weight, etc.).
3. Print out **`fruit_details`** to confirm it’s correct.
4. Commit and push your changes with a descriptive message (e.g., “Add fruit details dictionary”).

### 5. Track Out-of-Stock Fruits with Sets (Team Member C)

1. Pull the latest changes from the repository to ensure you have the notebook updates.
2. Create a set called **`out_of_stock`** and add **one** fruit (from your `fruit_details` keys) to show it is currently unavailable.  
3. Print out **`out_of_stock`** to confirm your entry.
4. Simulate a restock:
   * Remove that fruit from **`out_of_stock`** (if it was there).
   * Add another fruit to the set.
5. Print out **`out_of_stock`** again to confirm the changes.
6. Commit and push your changes with a descriptive message (e.g., “Add out_of_stock set and update fruits”).

### 6. Adjust Pricing (Team Member D)

1. Pull the latest changes from the repository to have everyone’s additions.
2. Update **`fruit_details`** to reflect a price change for at least **one** fruit. For example:

   ```python
   fruit_details["bananas"]["price_per_lb"] = 1.1
   ```

3. Print out the updated **`fruit_details`** to verify the new price.
4. Commit and push your changes with a descriptive message (e.g., “Update banana price in fruit_details”).

### 7. Final Merge and Verification

1. Make sure everyone has pulled the latest changes and that all conflicts are resolved.
2. In your GitHub repository, check the final **`fruit_inventory.ipynb`** file to see everyone’s contributions.
3. **Congratulations!** You have collaborated on a Python notebook managing fruit inventory data using tuples, dictionaries, and sets.

---

## Advanced

If you want an extra challenge, try the following steps together as a team:

* **Batching with Tuples:**  
  Create a list of tuples, where each tuple represents a fruit shipment. For example, each tuple might contain `(fruit_name, number_of_boxes, cost_per_box)`. Then calculate the total cost of each shipment using a simple formula.

* **Nested Dictionaries:**  
  Expand `fruit_details` so each fruit has nested keys, such as:

  ```python
  fruit_details = {
      "apples": {
          "price_info": {"wholesale": 2.0, "retail": 2.5},
          "color": "red",
          "in_stock": True
      },
      ...
  }
  ```

  Print out the retail or wholesale price as needed.

* **Team Branching:**  
  Create separate branches for each feature (e.g., “feature-advanced-tuple”, “feature-nested-dict”) and then merge them back into the main branch after review.

---

## Extra Credit

For those looking to push further:

* **Set Operations:**  
  Create additional sets like `low_stock` or `on_sale` and experiment with **union**, **intersection**, and **difference** operations to see which fruits meet multiple conditions.
  
* **Error Handling:**  
  Write a small function that checks if a fruit is in `fruit_details`. If it isn’t, handle it gracefully by printing a message like “Fruit not found!”

* **Pull Requests and Code Reviews:**  
  Instead of committing directly to `main`, open a pull request for each feature and have another teammate review and approve it before merging.

---

## Deliverables

* A **Jupyter notebook** named `fruit_inventory.ipynb` containing:
  
  * A tuple named `fruit_batch` with at least five fruit names  
  * A dictionary named `fruit_details` with nested details for each fruit  
  * A set named `out_of_stock`, demonstrating adding and removing fruits  
  * One or more price updates within `fruit_details`  
  * Clear print statements showing the changes you made  

* The final `fruit_inventory.ipynb` file should be pushed to your **team GitHub repository**, including all team contributions.
