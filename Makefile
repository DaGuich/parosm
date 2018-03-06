install:
	@echo "Use python setup.py install"

genproto:
	protoc -I proto/ --python_out=parosm/parse/ proto/*
