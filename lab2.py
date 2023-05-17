#Analysis
#•	Perform an analysis of the following functions:

															
															
	function 1:														
															
	def function1(number):														
		total=0;					1								
															
		for i in range(0, number):					1(range) + n								
			x = (i+1)				2n								
			total+=(x*x)				2n								
															
		return total					1								
															
						T(n)	3+5n								
							O(n)								
															
															
															
	function 2:														
															
	def function2(number):														
		return  ((number)*(number+1)*(2*number + 1))/6								7					
															
									T(n)	7					
										O(1)					
															
															
															
															
															
	function 3:														
															
	def function3(list):														
		for i in range (0,len(list)-1):							3+n						
			for j in range(0,len(list)-1-i):						3+(n-1)						
				if(list[j]>list[j+1]):					2+(n-1) 			where 1 for (j+1) and 1 for comparison			
					tmp=list[j]				1+(n-1)						
					list[j]=list[j+1]				2+(n-1)			where 1 for (j=1) and 1 for =			
					list[j+1]=tmp				2+(n-1)			where 1 for (j=1) and 1 for =			
															
								T(n)	3+n*( 10n-10)= 10n^2-10n+3						
									O(n^2)						
															
															
															
															
															
	function 4:														
															
	def function4(number):														
		total=1				1									
		for i in range(1, number):				1+n									
			total*=(i+1)			2*n									
		return total				1									
															
					T(n)	3+3n									
						O(n)									
															
															
															
															
															
															
