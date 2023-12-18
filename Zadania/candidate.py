experience = 2
languages = ["python", "typescript", "javascript", "java"]
contractType = "b2b"
if experience >= 2 and "java" in languages and "python" in languages:
    if contractType == "b2b" or contractType == "employment":
        print("Kandydat jest przyjęty")
    else:
        print("Kandydat nie spełnia warunku zatrudnienia")
else:
    print("Kandydat nie spełnia podstawowych wymagań")
