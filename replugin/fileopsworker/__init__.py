# -*- coding: utf-8 -*-
# Copyright © 2014 SEE AUTHORS FILE
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
File Operations worker.
"""
import os

from reworker.worker import Worker


class FileOpsWorkerError(Exception):
    """
    Base exception class for FileOpsWorker errors.
    """
    pass


class FileOpsWorker(Worker):
    """
    Worker which handles file operations work..
    """

    def process(self, channel, basic_deliver, properties, body, output):
        """
        Handles file operations work from messages from the bus.

        *Keys Requires*:
            * message: the message to write out.
        """
        # Ack the original message
        self.ack(basic_deliver)
        corr_id = str(properties.correlation_id)
        # TODO


def main():  # pragma: no cover
    from reworker.worker import runner
    runner(FileOpsWorker)


if __name__ == '__main__':  # pragma nocover
    main()
