# SingularityHA
# Copyright (C) 2014 Internet by Design Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import data_to_emon
from multiprocessing import Process
import time
import logging	

logger = logging.getLogger("environment")

def signal_handler(signal, frame):
	logger.info("Got CTL+C")
	time.sleep(1)
        for job in jobs:
        	job.terminate()
                job.join()
        sys.exit(0)

def main():
	try:
		jobs = []
		p = Process(target=data_to_emon.main)
	        jobs.append(p)
	        p.start()
		signal.signal(signal.SIGINT, signal_handler)
	except KeyboardInterrupt:
		pass
