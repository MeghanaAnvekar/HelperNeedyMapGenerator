from logic import generateMapping

needy = [ [1,24],[2,9],[3,18], [4,4]]
helpers = [[11,25],[12,10],[13,16],[14,2]]


print(generateMapping(needy_ = needy, helpers = helpers))
#{1: [{11: 24}], 3: [{13: 16}, {14: 2}], 2: [{12: 8}, {11: 1}]}

needy = [ [1,24],[2,9],[3,18], [4,4]]
helpers = [[11,16],[12,10],[13,16],[14,2],[15,8],[16,1]]

print(generateMapping(needy_ = needy, helpers = helpers))
#{1: [{13: 16}, {15: 8}], 3: [{11: 16}, {14: 2}], 2: [{12: 8}, {16: 1}]}

needy = [ [1,24],[2,9],[3,18], [4,4]]
helpers = [[11,23],[12,10],[13,16],[14,2],[15,26]]
print(generateMapping(needy_ = needy, helpers = helpers))
#{1: [{15: 24}], 3: [{11: 18}], 2: [{12: 8}], 4: [{11: 4}]}

needy = [ [1,24],[2,9],[3,18], [4,4]]
helpers = [[11,25],[12,10],[13,16],[14,2],[15,26]]
print(generateMapping(needy_ = needy, helpers = helpers))
#{1: [{11: 24}], 3: [{15: 18}], 2: [{12: 8}, {11: 1}]}