import docker
import logging

log = logging.getLogger(__name__)

#https://docker-py.readthedocs.io/en/stable/


class DockerClient(object):
    def __init__(self):
        self.client = docker.from_env()

    def docker_container_run(self, container_name, cmd=None, detach=False):
        """
        docker run
        """
        if detach:
            container = self.client.containers.run(container_name, detach=True)
            return container
        else:
            return self.client.containers.run(container_name, cmd)

    def docker_container_list(self):
        """
        docker ps
        """
        return self.client.containers.list()

    def docker_image_pull(self, image_name, tag):
        """
        docker pull 
        """
        log.info("Pulling {}:{}".format(image_name, tag))
        image = self.client.images.pull("{}:{}".format(image_name,tag))
        return image

    def docker_image_push(self, image_name, tag):
        """
        docker push
        """
        pass

    def docker_container_get(self, container_id_or_name):
        """
        get specific container object given id or name
        """
        container = self.client.containers.get(container_id_or_name)
        return container