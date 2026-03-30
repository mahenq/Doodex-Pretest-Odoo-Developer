from __future__ import annotations
from typing import Iterable, TypedDict, List


class Project(TypedDict):
    name: str
    budget: int
    sub_projects: List["Project"]


def calculate_total_budget(projects: Iterable[Project]) -> int:
    def _sum_project(project: Project) -> int:
        return project["budget"] + sum(
            _sum_project(sub) for sub in project["sub_projects"]
        )

    return sum(_sum_project(project) for project in projects)


def print_projects(projects: Iterable[Project]) -> None:
    def _print(project: Project, level: int) -> None:
        indent = "  " * level  
        print(f"{indent}{project['name']}: {project['budget']}")
        for sub in project["sub_projects"]:
            _print(sub, level + 1)

    for project in projects:
        _print(project, 0)


# main
if __name__ == "__main__":
    projects: list[Project] = [
        {
            "name": "Alpha",
            "budget": 10000,
            "sub_projects": [
                {
                    "name": "Alpha-1",
                    "budget": 5000,
                    "sub_projects": [],
                },
                {
                    "name": "Alpha-2",
                    "budget": 3000,
                    "sub_projects": [
                        {
                            "name": "Alpha-2-A",
                            "budget": 1000,
                            "sub_projects": [],
                        }
                    ],
                },
            ],
        }
    ]

    print("Hasil Perhitungan")
    print_projects(projects)

    total = calculate_total_budget(projects)
    print(f"\nTotal = {total}")