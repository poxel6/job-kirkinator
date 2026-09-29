from dataclasses import dataclass
from urllib.parse import unquote


@dataclass
class Job:

    id: int
    title: str
    link: str

    @staticmethod
    def job_from_url(url: str):
        """
        https://jobvision.ir/jobs/1543612/%D8%A2%D9%82%D8%A7?
        row=24&pageSize=30&searchId=392621890009422884&score=20.36&ReferrerJobPosition=8
        """

        url_sections = url.split("/")
        """
        [0]: https:
        [-4]: jobvision.ir
        [-3]: jobs
        [-2]: 1543612
        [-1]: %D8%A2%D9%82%D8%A7?
        row=24&
        pageSize=30&
        searchId=392621890009422884&
        score=20.36&
        ReferrerJobPosition=8
        """

        job_id = int(url_sections[-2])
        job_url = url_sections[-1]

        """
        [0]: %D8%A2%D9%82%D8%A7
        [1]: row=24&
        pageSize=30&
        searchId=392621890009422884&
        score=20.36&
        ReferrerJobPosition=8
        """
        job_url_quoted = job_url.split("?")[0]
        job_title = unquote(job_url_quoted)
        job_link = "/".join(url_sections[:-1])
        return Job(job_id, job_title, job_link)
