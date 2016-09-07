import yaml

def update_config(fname):
    with open(fname) as f:
        d=yaml.load(f)
	print d
        d["es_host"]="search-bridgelogs-ed-fgc37p7jyn3y5l465bp7ik5lr4.us-east-1.es.amazonaws.com"
        d["es_port"]=443
    with open(fname, "w") as f:
    	yaml.dump(d, f, default_flow_style=False)
    
if __name__=="__main__":
    base_path="/uhome/kvenkatswammy/elasticalert/elastalert/"
    update_config(base_path+"config.yaml")

