import hashlib
import sys
import argparse

def argsParse(arguments):
	"""checksums.py files -a md5
	usage: checksums.py FILE [FILE ...] [-a ALGORITHM]
	positional arguments:
		FILE: file to hash 

	optional arguments: 
		ALGORITHM: md5, sha256, sha1 supported
	"""

	parser = argparse.ArgumentParser(description='checksums')
	parser.add_argument('-a', '--algorithm', action='store',  
						default='md5', dest='algorithm', help='hash algorithm to be used' )
	parser.add_argument('files', action='store', nargs='+', 
						help='files to be hashed')
	return parser.parse_args(arguments)

def main():	
	args = argsParse(sys.argv[1:])
	files, algorithm = args.files, args.algorithm

	for fileTohash in files:
		checksum = Checksums(fileTohash, algorithm)
		#print(fileTohash + ":" + checksum.cal())
		print(''.join([fileTohash, ':', checksum.cal()]))

class Checksums:
	"""calculate md5, sha1, sha256..."""

	def __init__(self, fileTohash, algorithm):
		self.fileTohash = fileTohash
		self.algorithm = algorithm

	def getHashTool(self):
		if self.algorithm in ('sha256', 'SHA256'):
			return hashlib.sha256()
		elif self.algorithm in ('md5', 'MD5'):
			return hashlib.md5()
		elif self.algorithm in ('sha1', 'SHA1'):
			return hashlib.sha1()
		else:
			return hashlib.md5()

	def cal(self):
		tool = self.getHashTool() 

		with open(self.fileTohash) as f:
			while True:
				data = f.read(128)
				if not data:
					break
				tool.update(data)

		return tool.hexdigest()


if __name__ == "__main__":
	main()


