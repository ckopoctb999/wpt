import pytest
import webdriver.bidi.error as error

pytestmark = pytest.mark.asyncio


@pytest.mark.parametrize("value", [None, False, 42, {}, []])
async def test_params_context_invalid_type(bidi_session, inline, value):
    with pytest.raises(error.InvalidArgumentException):
        await bidi_session.browsing_context.reload(context=value)


@pytest.mark.parametrize("value", ["", "somestring"])
async def test_params_context_invalid_value(bidi_session, inline, value):
    with pytest.raises(error.NoSuchFrameException):
        await bidi_session.browsing_context.reload(context=value)


@pytest.mark.parametrize("value", [None, "", 42, {}, []])
async def test_params_ignore_cache_invalid_type(bidi_session, new_tab, value):
    with pytest.raises(error.InvalidArgumentException):
        await bidi_session.browsing_context.reload(context=new_tab["context"],
                                                   ignoreCache=value)


@pytest.mark.parametrize("value", [False, 42, {}, []])
async def test_params_wait_invalid_type(bidi_session, inline, new_tab, value):
    with pytest.raises(error.InvalidArgumentException):
        await bidi_session.browsing_context.reload(context=new_tab["context"],
                                                   ignoreCache=False,
                                                   wait=value)


@pytest.mark.parametrize("value", ["", "somestring"])
async def test_params_wait_invalid_value(bidi_session, new_tab, value):
    with pytest.raises(error.InvalidArgumentException):
        await bidi_session.browsing_context.reload(context=new_tab["context"],
                                                   ignoreCache=False,
                                                   wait=value)
