
from heapq import heapify, heappop

def generateMapping(helpers, needy_):
	# Assuming the list contains the people from neighbouring areas only
	# item in helpers -> (user_id, supplies); supplies = bit vector representing the supplies helper has
	# item in needy   -> (needs,user_id); needs = bit vector representing the needs of needy people
	if not helpers or not needy_:
		return {}

	helpers.sort(key = lambda x:x[1])
	mapping = {}
	needy = [ (-x[1],x[0]) for x in needy_]
	def search(low, high, key):
		
		
		while low < high:
			#print(low,high)
			mid = (low + high)//2
			supplies = helpers[mid][1]
			if supplies == key:
				return mid
			elif supplies < key:
				low = mid+1
			else:
				high = mid
		#print(low,high)
		return low


	heapify(needy) 
	
	while needy and helpers:
		person = heappop(needy)
		needs = -person[0]
		person_id = person[1]

		matched_helper = search(0,len(helpers)-1,needs)
		#print('matched_helper = ',matched_helper, helpers)
		supplies = helpers[matched_helper][-1]
		#print("needy = ", person[-1], "helper = ",matched_helper , needs)

		while supplies & needs:
			supplies_found = (supplies & needs)
			if person_id not in mapping:
				mapping[person_id] = [{helpers[matched_helper][0]:supplies_found}]
			else:
				mapping[person_id].append({helpers[matched_helper][0]:supplies_found})
				
			supplies = supplies ^ supplies_found
			needs = needs ^ supplies_found

			if supplies == 0:
				helpers.pop(matched_helper)
				if not helpers:
					break
			else:
				helpers[matched_helper][1] = supplies
				helpers.sort(key = lambda x:x[1])

			if needs:
				matched_helper = search(0,len(helpers)-1,needs)
				supplies = helpers[matched_helper][-1]

	return mapping









