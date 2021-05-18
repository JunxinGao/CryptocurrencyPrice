FROM fnndsc/ubuntu-python3

# set timezome
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# set the working directory in the container
WORKDIR /src

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip3 install -r requirements.txt

RUN apt-get update && apt-get install -y git
RUN pip install -U git+https://github.com/scrapy/scrapyd.git

# copy the content of the local src directory to the working directory
COPY Scrapy /src
COPY run.sh /src

# command to run on container start
EXPOSE 6800
RUN mkdir /etc/scrapyd
ENTRYPOINT ["/bin/sh"]