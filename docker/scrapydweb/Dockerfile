FROM python:3.8

# set timezome
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# set the working directory in the container
WORKDIR /src

# install dependencies
RUN pip3 install scrapydweb==1.4.0

# # copy the content of the local src directory to the working directory
# COPY scrapydweb_settings_v10.py .

# command to run on container start
# ENTRYPOINT ["/bin/sh"]
CMD scrapydweb