import requests
import time
import sys

if __name__ == "__main__":
    # Set exit code
    exit_code = 0

    # Extract the pipeline name from arguments
    assert len(sys.argv)==3, "Please provide the gocd server and pipeline slug (and no other arguments): %s" % sys.argv[1:]
    gocd_server = sys.argv[1]
    pipeline_slug = sys.argv[2]

    # First, get the pipeline's history
    pipeline_history_url = '{0}/go/api/pipelines/{1}/history/0'.format(gocd_server, pipeline_slug)
    pipeline_history = requests.get(pipeline_history_url).json()

    pipeline_instance_id = pipeline_history['pipelines'][0]["natural_order"]
    pipeline_instance_url = '{0}/go/api/pipelines/{1}/instance/{2}'.format(
        gocd_server, pipeline_slug, pipeline_instance_id
    )

    time_elapsed = 0

    # Every 15 seconds, check if the pipeline's stages are all completed.
    while True:
        time.sleep(15)

        time_elapsed += 15
        if time_elapsed > 300:
            print "Script timed-out while waiting for pipeline to complete."
            exit_code = 1

        pipeline_instance = requests.get(pipeline_instance_url).json()

        for stage in pipeline_instance['stages']:
            if stage['result'] == "Failed":
                print "Pipeline execution failed at stage: {0}".format(stage['name'])
                exit_code = 1
                break

            if stage['result'] != "Passed":
                continue

        break

    if exit_code == 0:
        print "Pipeline instance {0} completed successfully!".format(pipeline_instance_id)

    exit(exit_code)
