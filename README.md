# Gradescope Websraper
This script webscrapes Gradescope! As a Senior Teaching Assistant for CS1332 (Data Structures & Algorithms) @ Georgia Tech, I wrote this to automate the quality assurance process for homework grading.

## File Structure
In order for the script to run successfully, your file structure should be organzied as follows:<br>
<img width="276" alt="Screenshot 2024-04-18 at 1 31 09 PM" src="https://github.com/emilyjwu/gradescope-webscraper/assets/108899560/c4f5e69c-236d-4b84-8e73-6626006ed181"><br>
The script is in the same root directory as all semesters (ex: `fall2023`, `spring2024`). A subdirectory for each homework is created for each semester (ex: `fall2023/hw1`).

# Running the script
1. Clone the repository <br>
```
git clone https://github.com/emilyjwu/gradescope-webscraper.git
```
2. Navigate to your root directory. Create a directory for the current semester, and a subdirectory for the current homework.
3. Create 4 empty HTML files in `semester/homeworkNumber`:
   - campusEfficiency.html <br>
   - campusSubmissions.html <br>
   - onlineEfficiency.html <br>
   - onlineSubmissions.html <br>
5. Fill `campusSubmissions.html`
   - Find the homework assignment on Gradescope
   - On the "Grade Submissions" tab, click on the submissions button next to "Feedback & Manual Grading"
     - You should see a list of all students and the TA who graded them
   - Click on the 3 dots on the top right-hand corner of your browser
   - Click More Tools -> Developer Tools -> Inspect Element
   - Click on the div container for the page
     - `<div class="l-content">`
   - Right click on the HTML element, and click Copy -> Copy Element
   - Paste the HTML code into `campusSubmissions.html`
6. Fill out campusEfficiency.html
   - Exit out of the inspect element pop-up
   - Click on any homework submission
   - Click on the magnifying glass next to "[-5] Efficiency 1"
     - You should see a list of all TAs who applied this deduction
   - Follow the steps above to get the div container
   - Paste the HTML code into `campusEfficiencies.html`
7. Repeat steps (5-6) for the online section
8. In the `gradescopeWebscraper.py` file, edit the block of code at the bottom <br>
  ```
  if __name__ == "__main__":
      main("spring2024", "hw8")
  ```
9. Run the script by calling  <br>
```
python gradescopeWebscraper.py
```
10. View the results in `output.csv`

