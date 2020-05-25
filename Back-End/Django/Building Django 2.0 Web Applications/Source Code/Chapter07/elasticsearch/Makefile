
default:
	grep -i '^[a-z]' ./Makefile

run_es:
	docker run -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" --name answerly_es docker.elastic.co/elasticsearch/elasticsearch:6.0.0

build_es:
	docker build docker/elastic_search -t answerly/elastic_search
