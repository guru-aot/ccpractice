curl -w "\n" \
-H "Accept: application/json" \
-F "deployment-name=foicc1" \
-F "enable-duplicate-filtering=true" \
-F "deploy-changed-only=true" \
-F "foisinglestageWF.bpmn=@/app/foisinglestageWF.bpmn" \
http://localhost:8080/engine-rest/deployment/create