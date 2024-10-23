import asyncio
import json

import pytest

from codereviewai.services import github_service
from tests import request_test_content


@pytest.fixture
def github_owner_repo():
    return 'K-K-Ju', 'test-str-counter'


@pytest.fixture
def github_repo_json_content(github_owner_repo):
    j = ''.join(request_test_content.T1.splitlines())
    return github_owner_repo[0], github_owner_repo[1], json.loads(j)

@pytest.fixture
def github_repo_processed_content(github_owner_repo):
    c = request_test_content.T2
    return github_owner_repo[0], github_owner_repo[1], c

@pytest.fixture
def github_repo_file_paths(github_owner_repo):
    file_paths = [('pom.xml', 'https://raw.githubusercontent.com/K-K-Ju/test-str-counter/master/pom.xml'),
                  ('src/main/java/org/example/App.java', 'https://raw.githubusercontent.com/K-K-Ju/test-str-counter/master/src/main/java/org/example/App.java')]
    return github_owner_repo[0], github_owner_repo[1], file_paths


def test_fetch_repo_contents(github_repo_content):
    content_json = asyncio.run(github_service.__fetch_repo_contents__(github_repo_content[0], github_repo_content[1]))
    assert content_json == github_repo_content[2]


def test_fetch_repo_contents_fails_on_invalid_url():
    with pytest.raises(Exception):
        asyncio.run(github_service.__fetch_repo_contents__('None', 'None'))

def test_get_repo_contents(github_repo_processed_content):
    contents = asyncio.run(github_service.get_repo_contents(github_repo_processed_content[0], github_repo_processed_content[1]))
    assert contents == github_repo_processed_content[2]

def test_traverse_repo(github_repo_file_paths):
    file_paths = asyncio.run(github_service.__traverse_repo__(github_repo_file_paths[0], github_repo_file_paths[1]))
    assert file_paths.__eq__(github_repo_file_paths[2])
