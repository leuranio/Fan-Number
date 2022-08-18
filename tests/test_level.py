from pytest import raises

from game.level import NoPreviousLevel


def test_quando_ir_para_o_proximo_level_ele_deve_ser_um(level):
    level.next_level()
    assert level.show_level() == 1


def test_quando_o_level_estiver_em_um_voltar_ao_anterior(level):
    level.next_level()
    level.previous_level()
    assert level.show_level() == 0


def test_quando_o_numero_de_leveis_for_zero_e_tentar_voltar_mais_um(level):
    with raises(NoPreviousLevel):
        level.previous_level()
