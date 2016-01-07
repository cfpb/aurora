#!/bin/env python
import os
from bs4 import BeautifulSoup

if __name__ == '__main__':

    # Determine file paths
    script_path = os.path.dirname(os.path.realpath(__file__))
    config_xml_path = os.path.join(os.getenv("GOCD_CONFIG_PATH", "/tmp"), "cruise-config.xml")

    # Open destination and source files, respectively
    config_xml = open(config_xml_path, "r")

    # Parse the config and pipeline files, then create a new pipeline group and insert the pipeline
    config_xml.seek(0)
    config_soup = BeautifulSoup(config_xml.read(), "xml")
    config_soup.select_one('pipelines[group="automated-test"]').extract()
    config_xml.close()

    # Output the modified contents
    config_xml = open(config_xml_path, "w")
    config_xml.seek(0)
    config_xml.write(config_soup.prettify())
    config_xml.truncate()
    config_xml.close()

    exit(0)
