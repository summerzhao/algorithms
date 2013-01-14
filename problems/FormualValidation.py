'''
	Problem: for a formual contains several variables and several operator (binary-operator), 
	and '(' and ')', have a function check if the formual is a syntax correct formual.
	
	Solution:
		1. take '(' and ')' as a sub formual, use recursive method to solve the problem, 
		and '(...)' should be take as a variable
		2. consider only binary operator, so variable and operator should appear in sequence, 
		one variable, one operator, ....
		3. the first char should be a variable
		
'''

def isVariable(char, index, formual, variableSet, operatorSet):
	'''
		determine a char or charset is a variable
		return the next index of the scan, since if occur a subset '(..)' it should continue 
			on the next char from ')'
	'''
	if char in variableSet:
		return index
	elif char == '(':
		#find the match ')' which is a last ')' in the string
		rindex = formual.rfind(')')
		if rindex < 0:
			return False
		else:
			result = checkFormual(formual[index:rindex], variableSet, operatorSet)
			if result:
				return rindex + 1;
	else:
		return False
		
def isOperator(char):
	'''
		determine a char is a operator
	'''
	if char in operatorSet:
		return True
	else :
		return False
	
'''
the recursive method to check the formual
'''
	
def checkFormual(formual, variableSet, operatorSet):	
	#print formual
	index = 0
	previousIsChar = False
	while index < len(formual):
		char = formual[index]
		index += 1	
		#if the first variable and previous char is not a char, this char should be a variable
		if index == 0 or not previousIsChar:
			result = isVariable(char, index, formual, variableSet, operatorSet)
			if(result):
				index = result;
				previousIsChar = True
				continue
			else:
				return False
		#if the previous char is a char, this char should be a operator
		elif previousIsChar:
			if (isOperator(char)):
				previousIsChar = False
				continue
			else:
				return False
		
	return True

'''
same function as the checkFormual, but not include sub function, have more if else cases, 
readability is not so good
'''

def checkFormual2(formual, variableSet, operatorSet):
	#print formual
	index = 0
	isFirst = True
	isBesideOperator = False
	while index < len(formual):
		char = formual[index]
		index+=1
		if char in variableSet:
			if isFirst or isBesideOperator:
				isFirst = False
				isBesideOperator = False
				continue
			else:
				return False
		elif char in operatorSet:
			if not isFirst and not isBesideOperator:
				isBesideOperator = True
				continue
			else:
				return False
		elif char == '(':
			if not isFirst and not isBesideOperator:
				return False
			else:
				rindex = formual.rfind(')')
				if rindex < 0:
					return False
				else:
					result = checkFormual(formual[index:rindex], variableSet, operatorSet)
					#print result
					if not result:
						return False
					else:
						index = rindex + 1;
						continue
		else:
			return False
		
	return True
				
		
		
		
#main function
if __name__ == '__main__':
	
	variableSet = ['x'];
	operatorSet = ['*']
	
	formual = "x*x*(x*x)"
	print checkFormual(formual, variableSet, operatorSet)
	
	formual = "x*x*(x**x)"
	print checkFormual(formual, variableSet, operatorSet)
	
	formual = "x*x*(x*x"
	print checkFormual(formual, variableSet, operatorSet)
	
	formual = "x*x*x*x)"
	print checkFormual(formual, variableSet, operatorSet)
	
	variableSet = ['x', 'y'];
	operatorSet = ['*', '/']
	
	formual = "x*y*(y/x)"
	print checkFormual(formual, variableSet, operatorSet)
	
	formual = "x*y(y/x)"
	print checkFormual(formual, variableSet, operatorSet)
	
	formual = "x*y/(y/(x*y)/x)"
	print checkFormual(formual, variableSet, operatorSet)
	
	