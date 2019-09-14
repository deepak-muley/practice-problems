import unittest
from dockerclient import DockerClient


class TestDockerClient(unittest.TestCase):

    def setUp(self):
        self.docker_client = DockerClient()

    def test_dockerclient_listargs(self):
        container = self.docker_client.docker_container_run("alpine", ["echo", "hello", "world"])
        print(container)

    def test_dockerclient_stringargs(self):
        container = self.docker_client.docker_container_run("alpine", "echo hello world")
        print(container)

    def test_dockerclient_detach(self):
        container = self.docker_client.docker_container_run("bfirsh/reticulate-splines", detach=True)
        print(container.name + " " + container.id)
        container.stop()

    def test_dockerclient_listcontainers(self):
        for container in self.docker_client.docker_container_list():
            #print(dir(container))
            """
            ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
            '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
            '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
            '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attach', 'attach_socket', 'attrs', 
            'client', 'collection', 'commit', 'diff', 'exec_run', 'export', 'get_archive', 'id', 
            'id_attribute', 'image', 'kill', 'labels', 'logs', 'name', 'pause', 'ports', 'put_archive', 
            'reload', 'remove', 'rename', 'resize', 'restart', 'short_id', 'start', 'stats', 'status', 
            'stop', 'top', 'unpause', 'update', 'wait']
            """
            print(container.name + " " + container.id)

    def test_dockerclient_get_container(self):
        container = self.docker_client.docker_container_run("bfirsh/reticulate-splines", detach=True)
        print(container.name + " " + container.id) 

        container2 = self.docker_client.docker_container_get(container.name)

        self.assertEqual(container, container2)
        
        print("Stopping container {}".format(container.id))
        container.stop()
        print("Stopping container {}".format(container2.id))
        container2.stop()

    def test_dockerclient_list_stop_containers(self):
        container = self.docker_client.docker_container_run("bfirsh/reticulate-splines", detach=True)
        print(container.name + " " + container.id)
                
        for container in self.docker_client.docker_container_list():
            print("Stopping container {}".format(container.id))
            container.stop()

    def test_dockerclient_pull_image(self):
        self.docker_client.docker_image_pull("alpine", "latest")

if __name__ == '__main__':
    unittest.main()
