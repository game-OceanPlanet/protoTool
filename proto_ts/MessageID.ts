module qmr {
	export class MessageID
	{
		/**
		 *
		 * @author coler 2018.12.11
		 * 消息ID自动生成，请勿修改
		 *
		 */
		/** 映射协议ID对应的协议名 */
		private static MSG_KEYS: qmr.Dictionary = new qmr.Dictionary();
		/** 游戏初始化调用 */
		public static init()
		{
			let self = this;
			let id:number;
			for (let p in self)
			{
				id = self[p];
				self.MSG_KEYS.set(id, p);
			}
		}

		/** 通过本类的协议ID映射协议名字 */
		public static getMsgNameById(id: number): string
		{
			return MessageID.MSG_KEYS.get(id)
		}
		
		$params$

	}
}