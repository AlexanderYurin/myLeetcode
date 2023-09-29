def interpret(command: str) -> str:
	return command.replace("()", "o").replace("(al)", "al")


assert interpret("G()(al)") == "Goal"
