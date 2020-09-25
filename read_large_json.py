import ijson

def parse_json(file_name):
	with open(file_name,'rb') as myfile:
		#load json iteratively
		parser = ijson.parse(myfile);
		for prefix, event, value in parser:
            		print('prefix={}, event={}, value={}'.format(prefix, event, value))

if __name__=='__main__':
	parse_json("train.json")
	
