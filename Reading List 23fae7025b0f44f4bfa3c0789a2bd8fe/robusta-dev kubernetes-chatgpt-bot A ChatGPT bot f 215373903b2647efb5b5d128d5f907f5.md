# robusta-dev/kubernetes-chatgpt-bot: A ChatGPT bot for Kubernetes issues.

Column: https://github.com/robusta-dev/kubernetes-chatgpt-bot/
Processed: No
created on: January 10, 2023 4:49 PM
topics: kubernetes, tech-stuff

# Introduction

A ChatGPT bot for Kubernetes issues. Ask ChatGPT how to solve your Prometheus alerts, get pithy responses.

No more solving alerts alone in the darkness - the internet has your back.

[](robusta-dev%20kubernetes-chatgpt-bot%20A%20ChatGPT%20bot%20f%20215373903b2647efb5b5d128d5f907f5/68747470733a2f2f63646e2e6c6f6f6d2e636f6d2f73657373696f6e732f7468756d626e61696c732f39363463643837333561383734323837613931353563373733323062646364622d776974682d706c61792e676966)

# How it works

Prometheus forwards alerts to the bot using a webhook receiver.

The bot asks ChatGPT how to fix your alerts.

You stockpile food in your pantry for the robot uprising.

The bot is implemented using [Robusta.dev](https://github.com/robusta-dev/robusta), an open source platform for responding to Prometheus alerts and Kubernetes events.

# Prerequisites

- A Slack workspace (for Teams/Discord support, please open an issue)

# Setup

1. [Install Robusta with Helm](https://docs.robusta.dev/master/installation.html)
2. Load the ChatGPT playbook. Add the following to `generated_values.yaml`:

```
playbookRepos:
 chatgpt_robusta_actions:
 url: "https://github.com/robusta-dev/kubernetes-chatgpt-bot.git"

customPlaybooks:
# Add the 'Ask ChatGPT' button to all Prometheus alerts
- triggers:
 - on_prometheus_alert: {}
 actions:
 - chat_gpt_enricher: {}

```

1. Add your [ChatGPT API key](https://beta.openai.com/account/api-keys) to `generated_values.yaml`. Make sure you edit the existing `globalConfig` section, don't add a duplicate section.

```
globalConfig:
 chat_gpt_token: YOUR KEY GOES HERE

```

1. 
    
    Do a Helm upgrade to apply the new values: `helm upgrade robusta robusta/robusta --values=generated_values.yaml --set clusterName=<YOUR_CLUSTER_NAME>`
    
2. 
    
    [Send your Prometheus alerts to Robusta](https://docs.robusta.dev/master/user-guide/alert-manager.html). Alternatively, just use Robusta's bundled Prometheus stack.
    

# Demo

Instead of waiting around for a real Prometheus alert, lets simulate a fake one.

1. Choose any running pod in your cluster
2. Use the robusta cli to trigger a fake alert on that pod:

```
robusta playbooks trigger prometheus_alert alert_name=KubePodCrashLooping namespace=<namespace> pod_name=<pod-name>

```

If you installed Robusta with default settings, you can trigger the alert on Prometheus itself like so:

```
robusta playbooks trigger prometheus_alert alert_name=KubePodCrashLooping namespace=default pod_name=prometheus-robusta-kube-prometheus-st-prometheus-0

```

# Promotional Images

Feel free to use the following image or create your own.

![](robusta-dev%20kubernetes-chatgpt-bot%20A%20ChatGPT%20bot%20f%20215373903b2647efb5b5d128d5f907f5/211615506-fb8ba31a-4569-4ab6-9504-f1e42457771e.png)

# More Resources

[Natan Yellin and Sid Palas livestreamed about this on YouTube](https://www.youtube.com/watch?v=jMR8M3Xqlzg) - relevant part starts at 38:54