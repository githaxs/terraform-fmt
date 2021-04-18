FROM hashicorp/terraform:0.14.10 as terraform

FROM public.ecr.aws/lambda/python:3.8 as deps
COPY --from=terraform /bin/terraform /bin/terraform

RUN yum install -y git

COPY requirements.txt .
RUN python3.8 -m pip install -r requirements.txt

COPY . .

# Command can be overwritten by providing a different command in the template directly.
CMD ["handler.lambda_handler"]
