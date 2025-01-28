# Gradescope Webscraper
This script webscrapes Gradescope! As a Senior Teaching Assistant for CS1332 (Data Structures & Algorithms) @ Georgia Tech, I updated this for the quality assurance process for homework grading. The adjustments made to the script reflect changes in the course and the grading process of TAs. 

## File Structure
In order for the script to run successfully, your file structure should be organzied as follows:<br>
```
root/
├── spring2025/
│   ├── hw1.html
│   ├── hw2.html
├── .gitignore
├── excludedTAs.txt
├── gradescopeScraper.py
├── output.csv
├── README.md
```
The script is in the same root directory as all semesters (ex: `fall2023`, `spring2025`). A submission file is created for each homework (ex: `/fall2023/hw1.html`).

The following section will set up this file structure.

# Running the script
1. Clone the repository <br>
```
https://github.com/sleong415/gradescope-webscraper.git
```
2. Navigate to your root directory. Create a directory for the current semester, and a subdirectory for the current homework.
3. Create an empty HTML file in `semester/`:
   - `hwXX.html` <br>
4. Fill out `hwXX.html`
   - Find the homework assignment on Gradescope
   - On the "Grade Submissions" tab, click on the submissions button next to "Feedback & Manual Grading"
     - You should see a list of all students and the TA who graded them
   - Ctrl + Shift + I, or...
      - Click on the 3 dots on the top right-hand corner of your browser
      - Click More Tools -> Developer Tools -> Inspect Element
   - Hover over the page until you find the submission container. Multiple tags work, but the most specific one is
     - `<table class="table dataTable no-footer" id="question_submissions">`

   - Right click on the HTML element, and click Copy -> Copy Element
   - Paste the HTML code into `hwXX.html`
5. In the `gradescopeWebscraper.py` file, edit the block of code at the bottom <br>
  ```
  if __name__ == "__main__":
      main("spring2024", "hw8")
  ```
6. Create a text file `excludedTAs.txt` in the root directory
7. Populate `excludedTAs.txt` with names of TAs that should be excluded from the script
      - Name should be the exact name from Gradescope
      - Each name should be on a newline
      - For example, I exclude the Homework Senior TA from all calculations. They often give large number of points (+25) for deadline extensions which would incorrectly skew the statistics.
8. Run the script by calling  <br>
```
python gradescopeWebscraper.py
```
9. View the results in `output.csv`

