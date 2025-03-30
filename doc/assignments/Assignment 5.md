# Visualizing Program Pathways with Sankey Diagrams

## Overview
In this assignment, you will use real (synthetic) student course pathway data from three majors within the CECS program:
- Data Science  
- Artificial Intelligence  
- Cybersecurity

Your goal is to transform and visualize this data using a Sankey diagram that shows how students move through the required courses in their respective majors. You will clean and reshape the data, filter to required courses only, extract transitions, and then plot the most common flows through the program.

You will submit both your code and an image of your final diagram.

---
## Data Files
The following files are available in the class repository at: `data/assignment_5/`
### 1. `course_pathways.csv`
This file contains individual student course history data.

| Column       | Description                                                 |
|--------------|-------------------------------------------------------------|
| StudentID    | Unique ID for each student                                  |
| Program      | Academic program (e.g., CECS or CS)                         |
| Major        | Major within the program                                    |
| CoursePath   | Ordered list of courses a student took (separated by `->`) |
Each course path contains both required and elective courses for that student’s major.
### 2. `course_catalog_by_major.csv`
This file identifies which courses are required or elective for each major.

| Column | Description                             |
|--------|-----------------------------------------|
| Major  | Name of the major (e.g., Data science)  |
| Course | Course title                            |
| Type   | Either `Required` or `Elective`         |

---
## Instructions
### Step 1: Filter and Prepare Data
1. Load both CSV files.
2. Filter `course_pathways.csv` to include only students in the CECS program majoring in:
   - Data science
   - Artificial intelligence
   - Cybersecurity
3. Split the `CoursePath` string into individual courses.
4. For each student, use `course_catalog_by_major.csv` to:
   - Identify the required courses for their major
   - Remove any electives from their course path
5. Retain only the ordered sequence of required courses.
### Step 2: Extract Transitions
For each student's required course sequence, extract consecutive transitions.  
For example, the path: *Intro to Python -> Data Wrangling -> Machine Learning*
should yield the transitions:
- Intro to Python → Data Wrangling  
- Data Wrangling → Machine Learning
Aggregate all transitions across all students. Count how many students made each transition.
### Step 3: Create the Sankey Diagram
Using either R or Python:
- Create a Sankey diagram using your aggregated transition data.
- Nodes should be course titles.
- Links should represent transitions with their frequency (weight).
- Only include required courses (no electives).
- The layout should flow from left to right.
- Label your nodes clearly.
---
## What to turn in
Submit both of the following on Canvas:
6. An image file (`.png` or `.jpg`) of your final Sankey diagram.  
   Upload this image via the designated submission method (Canvas or otherwise).
7. A link to your R or Python script on your personal GitHub repository.  
   This should be the full code used to load, process, and visualize the data.
---
## Notes
- Be careful to preserve course order when parsing paths.
- Use appropriate tools for text splitting and reshaping:
  - In R: `strsplit()`, `tidyr::separate_rows()`, etc.
  - In Python: `str.split()`, `pandas.melt()`, etc.
- You may optionally filter out very rare transitions (e.g., transitions that occur only once).
- Before plotting, validate your wrangling by inspecting a few example paths.
- Focus on a clean visual layout with minimal clutter.