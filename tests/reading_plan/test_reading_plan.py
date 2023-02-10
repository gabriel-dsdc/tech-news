import pytest
from unittest.mock import patch
from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501


def test_reading_plan_group_news(mock_news, mock_group_news):
    with patch(
        "tech_news.analyzer.reading_plan.find_news", return_value=mock_news
    ):
        result = ReadingPlanService.group_news_for_available_time(10)

        for index, readable in enumerate(result["readable"]):
            assert (
                readable["chosen_news"]
                == mock_group_news["readable"][index]["chosen_news"]
            )
            assert (
                readable["unfilled_time"]
                == mock_group_news["readable"][index]["unfilled_time"]
            )

        assert result["unreadable"] == mock_group_news["unreadable"]

        with pytest.raises(
            ValueError, match="Valor 'available_time' deve ser maior que zero"
        ):
            ReadingPlanService.group_news_for_available_time(0)
