FROM hashicorp/terraform:1.1.6 as terraform

FROM public.ecr.aws/lambda/python:3.8 as deps
COPY --from=terraform /bin/terraform /bin/terraform

RUN yum install -y git

ARG GITHUB_TOKEN
COPY requirements.txt .
RUN python3.8 -m pip install -r requirements.txt

COPY . .

# Command can be overwritten by providing a different command in the template directly.
CMD ["handler.lambda_handler"]
