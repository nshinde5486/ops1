from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import jinja2
import os


'''hosts = NamedTemporaryFile(delete=False)
hosts.write(rendered_inventory)
hosts.close()'''

pb = Play(
    playbook='test.yml',
    host_list="ops",     # Our hosts, the rendered inventory file
    runner_callbacks="runner_cb",
    private_key_file='id_rsa.pub'
)

results = pb.run()
print results


