#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following disclaimer
#    in the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the  nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# ---------------------------------------------------------------------------- #
# Linux image - Alpine
# ---------------------------------------------------------------------------- #
FROM alpine:latest


# ---------------------------------------------------------------------------- #
# Install Application requirements
# ---------------------------------------------------------------------------- #
RUN apk add python3
RUN apk add sqlite
RUN apk add make
RUN python3 -m pip install bottle
RUN python3 -m pip install pony
RUN python3 -m pip install PyYAML
RUN python3 -m pip install jinja2

# ---------------------------------------------------------------------------- #
# Copy Application 
# ---------------------------------------------------------------------------- #
COPY . /app
WORKDIR /app

# ---------------------------------------------------------------------------- #
# Clean db application and populate minimal db data
# ---------------------------------------------------------------------------- #
RUN make clean
RUN make populate

# ---------------------------------------------------------------------------- #
# Made executable the startup script.
# ---------------------------------------------------------------------------- #
RUN chmod 700 start.sh

# ---------------------------------------------------------------------------- #
# Set default TCP port ( Docker side)
# ---------------------------------------------------------------------------- #
EXPOSE 8080

# ---------------------------------------------------------------------------- #
# Start Application 
# ---------------------------------------------------------------------------- #
ENTRYPOINT [ "/app/start.sh"]
