# limegenerator

[Lime Survey](https://github.com/LimeSurvey/LimeSurvey) is the most
popular FOSS online survey tool on the web.

Unfortunately, creating a survey can be quite a drag.  A lot of mouse
click and drag is necessary.

Why not use csv?

If you put this into a file, say, `survey.csv`

```csv
group1,T5,This is 5-vote and text
group1,T,Whereas this is only text
group2,T,More text
group2,5,Does only 5-vote work?
```

... and run `limegenerator.py survey.csv > survey.txt`, you can go to _Lime -> Surveys -> Import a survey_.

Select _"Browse..."_ and choose _"Import survey"_.

Notice that LimeSurvey _demands_ TSV (tab separated values) in a file
that ends with `.txt`.


Tada.  Your survey is ready.
