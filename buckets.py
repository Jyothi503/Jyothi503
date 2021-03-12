from decimal import *

def distribution(buck,n,lit):
	output=[]
	newlist=[]
	my_formatted_list=[]
	setl=len(set(buck))
	if setl==1:
		lit=min(lit/n,buck[0])
		for i in range(0,n):
			output.append(lit)
		my_formatted_list = [ float(Decimal('%.2f' % elem)) for elem in output ]
		return my_formatted_list	

	else:
		minim=min(buck)
		for i in range(0,n):
			output.append(minim)
		#print(output)
		for i in range(0,n):
			z=buck[i]-minim
			newlist.insert(i,z)
		remainlit=lit-sum(output)
		#print(remainlit)
		j=1
		flag=1
		while flag:
			if sum(newlist)!=0:
		
				minim=remainlit/(n-j)
				#print(minim)
				for i in range(0,n):
					x=min(newlist[i],minim)
					output[i]=output[i]+x
					newlist[i]=newlist[i]-x
					#print(newlist,output)
				j=j+1
				remainlit=lit-sum(output)
			if (sum(newlist)==0 and remainlit!=0) or (sum(newlist)!=0 and remainlit==0) or (sum(newlist)==0 and remainlit==0):
				flag=0
			
													
		my_formatted_list = [ float(Decimal('%.2f' % elem)) for elem in output ]				
		return my_formatted_list 			
			
									
	




"""n=int(input("No of bukets"))
lit=float(input("No of Liters"))
bucket=[]
print("Enter capacity of buckets")
for i in range(0,n):
	ele=float(input())
	bucket.append(ele)

print(distribution(bucket,n,lit))"""

