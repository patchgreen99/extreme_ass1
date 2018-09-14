

import re
import pandas as pd

with file('edit.txt') as f:
    data = []
    regex = ' ([A-Z0-9\-]{1,8})\n *(PGR|PGT|UG1|UG2|UG3|UG4|UG5|PT1|VUG|PT2)\n *([0-9]+)\n *([0-9]+)\n *([0-9]+)\n *([0-9]+)\n *(NA| *([0-9\-]+)\n *([0-9\-]+)\n *([0-9\-]+)\n *([0-9\-]+)\n *([0-9\-]+)\n *([0-9\-]+)\n)'
    for course, year, exam, overall, coursework, count, no_results, ave_exam, ave_overall,ave_coursework,dev_exam, dev_overall, dev_coursework in re.findall(regex, f.read(), flags=re.S):
        dic = {}
        dic['course']=course
        dic['year']=year
        dic['exam']=exam
        dic['count']=count
        dic['overall']=overall
        dic['coursework']=coursework
        dic['no_results']=no_results
        dic['ave_exam']=ave_exam
        dic['ave_overall']=ave_overall
        dic['ave_coursework']=ave_coursework
        dic['dev_exam']=dev_exam
        dic['dev_overall']=dev_overall
        dic['dev_coursework']=dev_coursework
        data.append(dic)

    pd.DataFrame(data).to_csv('input.csv')