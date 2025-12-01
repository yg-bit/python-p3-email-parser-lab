import re


class EmailAddressParser:
	def __init__(self, addresses):
		self.addresses = addresses

	def parse(self):
		"""Return a list of unique email addresses sorted alphabetically.

		Uses a regular expression to find email-like strings in the
		original input, then de-duplicates and sorts them.
		"""
		if not self.addresses:
			return []

		# A reasonably permissive email regex for the exercise
		pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

		found = re.findall(pattern, self.addresses)

		# unique and sorted alphabetically
		unique_sorted = sorted(set(found))

		return unique_sorted