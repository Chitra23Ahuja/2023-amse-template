# AMSE/SAKI 2023 Template Project
This template project provides some structure for your open data project in the AMSE/SAKI module.
This repository contains (a) a data science project that is developed by the student over the course of the semester, and (b) the exercises that are submitted over the course of the semester.
Before you begin, make sure you have [Python](https://www.python.org/) and [Jayvee](https://github.com/jvalue/jayvee) installed. We will work with [Jupyter notebooks](https://jupyter.org/). The easiest way to do so is to set up [VSCode](https://code.visualstudio.com/) with the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).

## Project Setup
The following files are part of this template repository as examples and should be **replaced by you** over the semester:

- `AMSE_database.sqlite`: Your final, cleaned dataset. You will create an automated data pipeline that creates this SQLite database from multiple open data sources. The template repository includes datasources about e-charging stations in germany of 2 datasources Germany: E-charging stations and  E-Ladesäulenregister.
- `exploration.ipynb`: A Jupyter notebook that you can use to explore your data and show in detail what it looks like. You can refer to this file in your report for users that want more information about your data.
- `report.ipynb`: Your final report as a Jupyter notebook. This is the result of your project work and should lead with a question that you want to answer using open data. The content of the report should answer the question, ideally using fitting visualizations, based on the data in `AMSE_database.sqlite`.


## Exercises
During the semester you will need to complete exercises, sometimes using [Python](https://www.python.org/), sometimes using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.<jv or py>`.

In regular intervalls, exercises will be given as homework to complete during the semester. We will divide you into two groups, one completing an exercise in Jayvee, the other in Python, switching each exercise. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://amse.uni1.de/). At the end of the semester, you will therefore have the following files in your repository:

1. `./exercises/exercise1.jv` or `./exercises/exercise1.py`
2. `./exercises/exercise2.jv` or `./exercises/exercise2.py`
3. `./exercises/exercise3.jv` or `./exercises/exercise3.py`
4. `./exercises/exercise4.jv` or `./exercises/exercise4.py`
5. `./exercises/exercise5.jv` or `./exercises/exercise5.py`

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). To view your exercise feedback, navigate to Actions -> Exercise Feedback in your repository (or use the direct link [/actions/workflows/exercise-feedback.yml](/actions/workflows/exercise-feedback.yml)).

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
		
Grading Exercise 2
	Overall points 24 of 24
	---
	By category:
		Shape: 5 of 5
		Types: 17 of 17
		Quality: 2 of 2

Grading Exercise 3
	Overall points 22 of 22
	---
	By category:
		Shape: 4 of 4
		Types: 14 of 14
		Quality: 4 of 4
```
