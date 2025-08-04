import marshal

with open("original.py", "r") as file: 
    code = file.read()

compiled = compile(code, '', 'exec')
with open("encoded.py", "w") as f:
    f.write("import marshal\nexec(marshal.loads(" + repr(marshal.dumps(compiled)) + "))")
