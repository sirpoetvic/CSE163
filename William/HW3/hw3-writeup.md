# Overview
Complete this 'readme.md' file when you answer the questions in Part 3 of the [Handout](https://courses.cs.washington.edu/courses/cse163/21wi/hw3/spec.html). There is no `hw3-written.txt` file (mentioned in the online directions).   

Be sure to add your answers inside a ```code block``` to make it easy for me to find your answers.

For help on using Markdown, see [Markdown](https://gist.github.com/cuonggt/9b7d08a597b167299f0d)

## Instructions
Review the source of the dataset [here](https://nces.ed.gov/programs/digest/d18/tables/dt18_104.20.asp). For the following reflection questions consider the accuracy of data collected, and how it's used as a public dataset (e.g. presentation of data, publishing in media, etc.). All of your answers should be complete sentences and show thoughtful responses. "No" or "I don't know" or any response like that are not valid responses for any questions. There is not one particularly right answer to these questions, instead, we are looking to see you use your critical thinking and justify your answers!

### #1: Plotting questions
1. Do you think the bar chart from part 1b is an effective data visualization? Explain in 1-2 sentences why or why not.
```
Yes, since we are comparing, it's easiest to see the disparities (though minimal in this scenario) with a bar graph. Something like a line graph would see more of the trends, while a bar graph mainly focuses on comparison.
```
2. Why did you choose the type of plot that you did in part 1c? Explain in a few sentences why you chose this type of plot.
```
For plot_hisplabic_min_degree.png, I used a linear regression plot. I believe that this is a good plot in this situation because we're trying to see the disparities of how people with high school and bachelor's degree's changed over the years (i.e. the trends), which can be seen with a line plot, but having a regression with datapoints helps to see outliers, and more or less given the dataset.
```

### #2: Datasets
Datasets can be biased. (i.e. The data can be WRONG!)
Bias in data means it might be skewed away from or portray a wrong picture of reality. 
The data might contain inaccuracies or the methods used to collect the data may have 
been flawed. Describe a possible bias present in this dataset and why it might have 
occurred. Your answer should be about 2 or 3 sentences long. Again, describe how
the data is incorrect. (Note: incomplete is not necessarily the same as incorrect.)
```
There is a very good chance that the data is collected in a specific area that caters more towards one or more demographics; from urban areas, neglecting rural populations.That is, data and trends will be more biased towards those specific demographics, genders, groups, etc... Cities that are bigger are more likely to be more diverse, than those without them. This causes bias.

```
### #3: Context
Later in the class we will talk about ethics in data science. Question #3 here is 
supposed to be a warm-up to get you thinking about our responsibilities when processing
data, to get you to think about both the intended and unintended consequences of
actions driven by data. 

Good intentions don’t insure good outcomes. Many people have good inten\tions yet cause very real 
harm in the world. We’ll discuss specific examples of well-intentioned algorithms 
perpetuating more harm later. In computing, that harm is magnified, 
automated, and reproduced by computers.

Describe a **policy** or **decision** motivated by this dataset with the 
intended goal of improving educational equity but which ultimately exacerbates 
the problem or causes a new one. How can the policy (or decision) lead to further 
injustice even when designed with equity in mind? In other words, we are trying 
to think of a way that we could use this data with good intentions, but actually 
would end up causing harm. 
```
Decision: given the data, provide better opportunities for men to acheive higher education like Masters.

This policy makes the problem worse, as it is a known fact that masters programs are predominately filled by men, which isn't great. As such, more men would have more opportunities to get masters, which goes against current initatives and holistic statistics that women get more masters degrees with this dataset specifically.
```
