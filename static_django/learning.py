from experta import KnowledgeEngine, Fact, Field, DefFacts, Rule, MATCH, TEST, AS, OR, AND


""" Fibonacci Series """
class FibonacciDigit(Fact):
	position = Field(int, mandatory=True)
	value = Field(int, mandatory=True)


class FibonacciCalculator(KnowledgeEngine):
	# Fact method (to be called inside Rules)
	@DefFacts()
	def set_target_position(self, target):
		print("set_target_position")
		# Add Fact to fact list
		yield Fact(target_position=target)  # Set target position as a Fact

	# Reserved name, initial function
	@DefFacts()  # Setting up expert system
	def init_sequence(self):
		print("init_sequence")
		# Init the fibonacci sequence declaring first and second value as 1
		yield FibonacciDigit(position=1, value=1)
		yield FibonacciDigit(position=2, value=1)

	@Rule(
		# Fact: get a FibonacciDigit and assign its values to MATCH.pos_1 and MATCH.val_1
		FibonacciDigit(
			position=MATCH.pos_1,
			value=MATCH.val_1),
		# Fact: get a FibonacciDigit and assign its values to MATCH.pos_2 and MATCH.val_2
		FibonacciDigit(
			position=MATCH.pos_2,
			value=MATCH.val_2),
		# Test: pos_2 should be pos_1 + 1
		TEST(lambda pos_1, pos_2: pos_2 == pos_1 + 1),
		# Fact: digit's position should be before target_position
		Fact(target_position=MATCH.t),
		# Test: compute digit before target_position
		TEST(lambda pos_2, t: pos_2 < t))
	def compute_next(self, pos_2, val_1, val_2):
		print("compute_next")
		next_digit = FibonacciDigit(position=pos_2+1, value=val_1+val_2)
		self.declare(next_digit)  # Add to Fact list

	@Rule(
		Fact(target_position=MATCH.t),
		FibonacciDigit(position=MATCH.t, value=MATCH.val))
	def print_last(self, t, val):
		print("print_last")
		print("El numero de Fibonacci en la posicion #%s es %s"%(t, val))


""" Factorial """
class Factorial(Fact):
	# Declare object
	# position is a number equal or higher than 0
	position = Field(lambda n: isinstance(n, int) and n >=0, mandatory=True)
	value = Field(int, mandatory=True)

class FactorialCalculator(KnowledgeEngine):
	@DefFacts()
	def first(self):
		yield Factorial(position=1, value=1)

	@Rule(
		AS.factorial << Factorial(position=MATCH.p, value=MATCH.v))
	def factorial(self, factorial, p, v):
		self.declare(Factorial(position=p+1, value=(p+1)*v))
		#self.retract(factorial)  # Delete temporary Fact used to calc next factorial


""" TestOrMatches """
settings = {"umbral": 0.75}
class TestOrMatches(KnowledgeEngine):
	@DefFacts()
	def declare_three_facts(self):
		yield Fact(prob=.82, tag="3")
		yield Fact(prob=.75, tag="7")
		yield Fact(prob=.33, tag="12")

	# Diagnostic N°7
	@Rule(
		Fact(prob=MATCH.p, tag=MATCH.t),
		TEST(lambda t: t=="7"),
		TEST(lambda p: p>=settings.get('umbral')))
	def test07(self, p, t):
		print("--- test07")
		print("prob: %s"%p)
		print("tag: %s"%t)

	# Diagnostic N°3
	@Rule(
		Fact(prob=MATCH.p, tag=MATCH.t),
		TEST(lambda t: t=="3"),
		TEST(lambda p: p>=settings.get('umbral')))
	def test03(self, p, t):
		print("--- test03")
		print("prob: %s"%p)
		print("tag: %s"%t)

	# Diagnostic #9
	@Rule(OR(
		AND(
			Fact(tag=MATCH.tag, prob=MATCH.prob),
			TEST(lambda tag: tag=="3")),
		AND(
			Fact(tag=MATCH.tag, prob=MATCH.prob),
			TEST(lambda tag: tag=="5")),
		AND(
			Fact(tag=MATCH.tag, prob=MATCH.prob),
			TEST(lambda tag: tag=="12")),
		))
	def action(self, prob, tag):
		pass


# START function
def start():
	"""
	print("# FibonacciCalculator")
	f = FibonacciCalculator()
	f.reset(target=7)
	f.run()
	print("--- Fact list ---")
	print(f.facts)
	print("# FactorialCalculator")
	f = FactorialCalculator()
	f.reset()
	f.run(5)
	print("--- Fact list ---")
	print(f.facts)
	"""
	print("# TestOrMatches")
	f = TestOrMatches()
	f.reset()
	print("--- Fact list ---")
	print(f.facts)
	print("--- Run ---")
	f.run()


if __name__ == "__main__":
	print("START")
	start()
#
