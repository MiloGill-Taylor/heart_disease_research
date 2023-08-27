import csv
import matplotlib.pyplot as plt 

ppl_heart_disease=[]
ppl=[]
ppl_healthy=[]
category_dict={}

def mean_calc(lst):
	sum=0
	for num in lst:
		sum+=num
	return sum/len(lst)

with open('heart.csv') as heart_file:
	heart_reader=csv.reader(heart_file, delimiter=',')
	row_count=0
	for row in heart_reader:
		if row_count==0:
			for i in range(len(row)):
				category_dict[row[i]]=i
		elif row[category_dict['target']]=="1":
			#person has heart disease
			ppl_heart_disease.append(row)
			ppl.append(row)
		else:
			#healthy person
			ppl_healthy.append(row)
			ppl.append(row)
		row_count+=1



ages_heart_disease=[]
for person in ppl_heart_disease:
	age=person[0]
	ages_heart_disease.append(int(age))
ages_heart_disease.sort()


ages_all=[]
for person in ppl:
	age=person[0]
	ages_all.append(int(age))
ages_all.sort()

ages_healthy=[]
for person in ppl_healthy:
	age=person[0]
	ages_healthy.append(int(age))
ages_healthy.sort()

mean_age_heart_disease=mean_calc(ages_heart_disease)
mean_age=mean_calc(ages_all)
mean_age_healthy=mean_calc(ages_healthy)

print(mean_age_heart_disease)
print(mean_age)
print(mean_age_healthy)

#plt.hist(ages_heart_disease, bins=10,histtype='stepfilled')
#plt.show()









