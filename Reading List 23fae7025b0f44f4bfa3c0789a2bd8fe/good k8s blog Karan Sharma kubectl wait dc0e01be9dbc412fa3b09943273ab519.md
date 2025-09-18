# good k8s blog Karan Sharma | kubectl wait

Column: https://mrkaran.dev/posts/kubectl-wait/
Processed: No
created on: March 28, 2022 12:49 PM
topics: azure, kubernetes, tech-stuff

For the longest time I've had these commands in my `.gitlab-ci.yml` file for a K8s CD pipeline:

```
...
    - kubectl apply -k overlays/prod
    - echo "Waiting for 15 seconds for pods to be restarted" && sleep 15
    - kubectl get po
    ...

```

So, basically I apply the changes to cluster using `kubectl apply` and wait for arbitary decided time (15 seconds) to see the pod `status`, hoping by that time the new deployments would have been active and old pods would be deleted. As the traditional SRE saying goes *Hope is not a strategy* this was clearly hacky and I knew it back then, just didn't priortise enough to find a replacement. Recently got to know about `kubectl wait` and woah, this is exactly what I needed. I can wait till either the condition is true or a timeout happens, whichever is earlier. This is so much better than the previous *hack*.

```
kubectl wait --for=condition=available --timeout=60s --all deployments

```

Here the `condition` depends on the resource you are selecting. You can see the values for `Conditions` using `kubectl describe <resource>`. For eg, for deployment and pods:

```
$ kc describe deployments/{deployment_name} | grep Conditions -A 5
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Progressing    True    NewReplicaSetAvailable
  Available      True    MinimumReplicasAvailable

```

```
$ kc describe pods/{pod_name} | grep Conditions -A 5
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True

```

So, now you'll set the value for `condition` according to your choice. This will be pretty useful in CI/CD pipelines. That's pretty much it.

Unrelated, but I thought about doing more such *short* posts and be consistent with more of writing. If you liked the short and precise format or have any feedback on it, do reach out to me on [Twitter](https://twitter.com/@mrkaran_).

Happy New Year :)

Fin!