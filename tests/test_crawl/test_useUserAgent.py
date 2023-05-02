from usepy import useUserAgent


def test_user_agent():
    assert useUserAgent() in useUserAgent.pc_user_agents
    assert useUserAgent(pc=False) in useUserAgent.mobile_user_agents
