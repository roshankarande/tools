FROM ubuntu

RUN apt-get update \
	&& apt-get install -y \
	curl \
	git \

	python3 \
	python3-pip \
	sudo \
	vim \
	wget \
	&& rm -rf /var/lib/apt/lists/*


# golang \

RUN echo ${PATH}
RUN curl -fsSL https://code-server.dev/install.sh | sh -s -- --method=standalone --prefix=/tmp/code-server
# RUN curl -LsSf https://astral.sh/uv/install.sh | sh


RUN pip3 install uv --break-system-packages
# RUN curl -fsSL https://raw.githubusercontent.com/filebrowser/get/master/get.sh | bash

# ENV PATH="${PATH}:/home/${USER}/.cargo/bin"

# RUN ["/bin/bash", "-c", "/home/roshan/.cargo/bin/uv venv"]
# RUN echo '. "$HOME/.venv/bin/activate"' >>  ~/.bashrc
# RUN echo '. "$HOME/.venv/bin/activate"' >>  ~/.zshrc


ARG USER=coder
RUN useradd --groups sudo --no-create-home --shell /bin/bash ${USER} \
	&& echo "${USER} ALL=(ALL) NOPASSWD:ALL" >/etc/sudoers.d/${USER} \
	&& chmod 0440 /etc/sudoers.d/${USER}
USER ${USER}


WORKDIR /home/${USER}
