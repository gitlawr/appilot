from langchain.schema.language_model import BaseLanguageModel
from kubernetes import config

from k8s import context
from k8s.tools.helm.tool import (
    DeleteApplicationTool,
    DeployApplicationTool,
    GenerateUpgradeApplicationValuesTool,
    GetApplicationAccessEndpointsTool,
    GetApplicationDetailTool,
    ListApplicationsTool,
    SearchChartTool,
    UpgradeApplicationTool,
)
from k8s.tools.manage_resource.tool import (
    ApplyResourcesTool,
    ConstructResourceForUpdateTool,
    ConstructResourceTool,
    DeleteResourceTool,
    DescribePodTool,
    GetIngressAccessEndpointsTool,
    GetPodLogsTool,
    GetResourceDetailTool,
    GetResourceYamlTool,
    GetServiceAccessEndpointsTool,
    ListResourcesForInfoTool,
    ListResourcesTool,
    WatchResourcesTool,
)
from walrus.tools.general.tools import BrowseURLTool


class KubernetesToolKit:
    """Kubernetes toolkit."""

    llm: BaseLanguageModel

    def __init__(self, llm: BaseLanguageModel):
        self.llm = llm
        config.load_kube_config()
        context.init_api_resources_cache()

    def get_tools(self):
        llm = self.llm
        tools = [
            ListResourcesTool(return_direct=True),
            ListResourcesForInfoTool(),
            GetResourceDetailTool(),
            GetResourceYamlTool(return_direct=True),
            GetServiceAccessEndpointsTool(),
            GetIngressAccessEndpointsTool(),
            GetPodLogsTool(),
            DescribePodTool(),
            WatchResourcesTool(return_direct=True),
            DeleteResourceTool(),
            ConstructResourceTool(llm=llm),
            ConstructResourceForUpdateTool(llm=llm),
            ApplyResourcesTool(),
            SearchChartTool(llm=llm),
            DeployApplicationTool(),
            GenerateUpgradeApplicationValuesTool(llm=llm),
            UpgradeApplicationTool(),
            ListApplicationsTool(),
            GetApplicationDetailTool(),
            GetApplicationAccessEndpointsTool(),
            BrowseURLTool(),
            DeleteApplicationTool(),
        ]
        return tools
