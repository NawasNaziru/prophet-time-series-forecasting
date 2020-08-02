# Answers for Peer review
1. Are there unit tests for the API?
* Yes, in folder unittests -> ApiTests.py
2. Are there unit tests for the model?
* Yes, in folder unittests -> ModelTests.py
Are there unit tests for the logging?
* Yes, in folder unittests -> LoggerTests.py
Can all of the unit tests be run with a single script and do all of the unit tests pass?
* Yes -> run_tests.py
Is there a mechanism to monitor performance?
* Yes -> monitoring.py
Was there an attempt to isolate the read/write unit tests from production models and logs?
* Yes -> prophet_model.py & logger.py
Does the API work as expected? For example, can you get predictions for a specific country as well as for all countries combined?
* Worked for me. I am happy to hear if you manage to break it.
Does the data ingestion exists as a function or script to facilitate automation?
* script
Were multiple models compared?
* Yes -> Model_validation.ipynb
Did the EDA investigation use visualizations?
* Yes. -> EDA.ipynb
Is everything containerized within a working Docker image?
* Yes -> Dockerfile
Did they use a visualization to compare their model to the baseline model?
* No.

# IBM AI Enterprise Workflow Capstone
This is a time series prediction application for the IBM AI Enterprise Workflow Capstone project. 
The application utilized Facebook's Prophet algorithm, as well as datasets provided by the course.

This project contains 
* Unit tests for API, logging, and model
* run_tests.py for running all tests with a single script
* monitoring.py for performance monitoring
* Model_validation.ipynb for model comparison
* EDA.ipynb for data analysis
* Docker deployment

Usage notes
===============

All commands are from this directory.

To test app.py
---------------------

.. code-block:: bash

    ~$ python app.py
    
To test the model directly
----------------------------

see the code at the bottom of `prophet_model.py`

.. code-block:: bash

    ~$ python prophet_model.py

To build the docker container
--------------------------------

.. code-block:: bash

    ~$ docker build --tag prophet_app .

Check that the image is there.

.. code-block:: bash

    ~$ docker image ls
    
You may notice images that you no longer use. You may delete them with

.. code-block:: bash

    ~$ docker image rm IMAGE_ID_OR_NAME

And every once and a while if you want clean up you can

.. code-block:: bash

    ~$ docker system prune


Run the unittests
-------------------

Before running the unit tests launch the `app.py`.

To run only the api tests

.. code-block:: bash

    ~$ python unittests/ApiTests.py

To run only the model tests

.. code-block:: bash

    ~$ python unittests/ModelTests.py


To run all of the tests

.. code-block:: bash

    ~$ python run-tests.py

Run the container to test that it is working
----------------------------------------------    

.. code-block:: bash

    ~$ docker run -p 4000:8080 prophet_app


